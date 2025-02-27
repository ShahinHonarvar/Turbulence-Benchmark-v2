def get_palindromes(text, min_length):
    palindromes = set()
    for i in range(len(text) - min_length + 1):
        for j in range(min_length, len(text) - i + 1):
            substring = text[i:i + j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes

def palindrome_of_length_at_least_n(string, n=55):
    return get_palindromes(string, n)