def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1] and len(word) >= 3
    index_range = range(1, 8)
    letters = set(s.lower())
    palindromes = set()
    for left in index_range:
        for right in index_range:
            if left <= right:
                subsequence = ''.join(sorted([letter for letter in s[left - 1:right] if letter in letters]))
                if is_palindrome(subsequence):
                    palindromes.add(subsequence)
    return palindromes