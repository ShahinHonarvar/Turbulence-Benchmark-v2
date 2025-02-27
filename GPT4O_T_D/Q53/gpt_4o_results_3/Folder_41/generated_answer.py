def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def find_palindromes(s, length):
        palindromes = set()
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
        return palindromes
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    current_length = 28
    while current_length <= len(s):
        palindromes = find_palindromes(s, current_length)
        result.update(palindromes)
        current_length += 1
    return result