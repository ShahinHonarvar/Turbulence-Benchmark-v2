def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    input_string = ''.join(filter(str.isalpha, s)).lower()
    length = 60
    palindromes = set()
    for i in range(len(input_string) - length + 1):
        substring = input_string[i:i + length]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes