def palindromes_between_indices(s):
    subset = ''.join((c for c in s[2:9] if c.isalpha())).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, left, right):
        if left >= 0 and right < len(subset) and (subset[left] == subset[right]):
            generate_palindromes(subset[left] + current + subset[right], left - 1, right + 1)
        if len(current) >= 6:
            palindromes.add(current)
    for i in range(len(subset)):
        generate_palindromes(subset[i], i - 1, i + 1)
        generate_palindromes(subset[i] + subset[i + 1], i - 1, i + 2)
    return palindromes