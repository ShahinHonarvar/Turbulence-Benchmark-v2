def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        sub = ''.join(filter(str.isalpha, sub))
        return sub.lower() == sub[::-1].lower()
    n = 37
    palindromes = set()
    filtered_s = ''.join(filter(str.isalpha, s))
    length = len(filtered_s)
    for start in range(length):
        for end in range(start + n, length + 1):
            substring = filtered_s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes