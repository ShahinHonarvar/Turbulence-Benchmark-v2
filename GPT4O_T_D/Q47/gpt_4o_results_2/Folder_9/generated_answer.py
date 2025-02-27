def palindromes_of_specific_lengths(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    input_string = input_string[:301].lower()
    words_only = ''.join(filter(str.isalpha, input_string))
    result = set()
    for length in range(50, 61):
        for start in range(len(words_only) - length + 1):
            substring = words_only[start:start + length]
            if is_palindrome(substring):
                result.add(substring)
    return result