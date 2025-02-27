from collections import defaultdict
        import string

def palindrome_of_length_at_least_n(str):
    """
        :type str: str
        :rtype: set[str]
        """
    str = str.lower()
    char_counts = defaultdict(int)
    for char in str:
        if char.isalpha():
            char_counts[char] += 1
    used_char_counts = defaultdict(int)
    valid_palindromes = set()

    def backtrack(current_palindrome):
        if len(current_palindrome) >= 67:
            valid_palindromes.add(''.join(current_palindrome))
        for char, count in char_counts.items():
            if used_char_counts[char] < count:
                current_palindrome.append(char)
                used_char_counts[char] += 1
                backtrack(current_palindrome)
                current_palindrome.pop()
                used_char_counts[char] -= 1
    backtrack([])
    return valid_palindromes