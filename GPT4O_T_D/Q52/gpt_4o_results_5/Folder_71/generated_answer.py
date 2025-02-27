def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    processed_string = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(processed_string) - 77):
        substring = processed_string[i:i + 78]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes