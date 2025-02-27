def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    substring = s[2:6]
    unique_letters = set()
    for letter in substring:
        if letter.isalpha():
            unique_letters.add(letter.lower())
    length = len(unique_letters)
    output = set()
    for i in range(length):
        for j in range(i, length):
            for k in range(j, length):
                new_word = ''.join(unique_letters).lower()
                if is_palindrome(new_word[i:j + 1]):
                    output.add(new_word[i:j + 1])
    return output