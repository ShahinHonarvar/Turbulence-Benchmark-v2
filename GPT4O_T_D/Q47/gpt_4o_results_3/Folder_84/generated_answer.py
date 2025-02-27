def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    filtered_string = ''.join([c for c in s[23:78] if c.isalpha()]).lower()
    n = len(filtered_string)
    palindromes = set()
    for start in range(n):
        for end in range(start + 13, min(n, start + 41)):
            if is_palindrome(filtered_string[start:end + 1]):
                palindromes.add(filtered_string[start:end + 1])
    return palindromes