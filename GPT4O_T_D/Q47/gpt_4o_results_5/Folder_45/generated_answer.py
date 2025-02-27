def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    region = ''.join((char for char in s[70:141] if char.isalpha()))
    palindromes = set()
    length_region = len(region)
    for length in range(3, 61):
        for start in range(length_region - length + 1):
            substring = region[start:start + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes