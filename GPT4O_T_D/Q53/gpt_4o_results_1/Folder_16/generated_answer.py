def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    found_palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 119, length + 1):
            if is_palindrome(s[i:j]):
                found_palindromes.add(s[i:j])
    return found_palindromes