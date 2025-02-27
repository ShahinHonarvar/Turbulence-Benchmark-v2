from collections import Counter

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    if len(letters) < 6:
        return set()
    letter_counts = Counter(letters)
    palindromes = set()

    def generate_palindrome(current, remaining_counts):
        if len(current) >= 6:
            palindrome = ''.join(current)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
        for letter, count in remaining_counts.items():
            if count > 0:
                new_counts = remaining_counts.copy()
                new_counts[letter] -= 1
                generate_palindrome(current + [letter], new_counts)
    generate_palindrome([], letter_counts)
    return palindromes