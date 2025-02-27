from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome_possible(freq_count, length):
        odd_counts = sum((1 for count in freq_count.values() if count % 2 != 0))
        return odd_counts <= length % 2
    s = s[:6].lower()
    freq_count = Counter(filter(str.isalpha, s))
    palindromes = set()
    for possible_length in range(4, 7):
        if is_palindrome_possible(freq_count, possible_length):
            half_chars = []
            odd_char = ''
            for char, count in freq_count.items():
                half_chars.extend(char * (count // 2))
                if count % 2 == 1 and odd_char == '':
                    odd_char = char
            half_permutations = set()

            def helper(perm, remaining):
                if not remaining:
                    half_permutations.add(''.join(perm))
                else:
                    for i in range(len(remaining)):
                        helper(perm + [remaining[i]], remaining[:i] + remaining[i + 1:])
            helper([], half_chars)
            for half in half_permutations:
                full_palindrome = half + odd_char + half[::-1] if possible_length % 2 == 1 else half + half[::-1]
                palindromes.add(full_palindrome)
    return palindromes