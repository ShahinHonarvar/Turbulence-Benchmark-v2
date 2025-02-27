def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    clean_string = ''.join(filter(str.isalpha, s)).lower()
    found_palindromes = set()
    n = len(clean_string)
    for i in range(n):
        for j in range(i + 67, n + 1):
            substring = clean_string[i:j]
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes