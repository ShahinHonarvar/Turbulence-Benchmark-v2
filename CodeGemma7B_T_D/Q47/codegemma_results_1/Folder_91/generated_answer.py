def palindromes_of_specific_lengths(string):

    def is_palindrome(word):
        word = ''.join(sorted(word))
        return word == word[::-1] and word.isalpha()
    output = set()
    for i in range(len(string)):
        for j in range(i + 3, min(i + 6, len(string))):
            word = string[i:j].lower()
            if is_palindrome(word):
                output.add(word)
    return output