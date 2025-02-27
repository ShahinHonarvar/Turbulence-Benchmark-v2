from string import ascii_letters

def palindrome_of_length_at_least_n(text):

    def is_palindrome(word):
        return word == word[::-1]
    filtered_text = ''.join([letter for letter in text if letter.lower() in ascii_letters])
    palindromes = set()
    for i in range(len(filtered_text)):
        for j in range(i + 1, len(filtered_text) + 1):
            word = filtered_text[i:j]
            if len(word) >= 28 and is_palindrome(word):
                palindromes.add(word)
    return palindromes