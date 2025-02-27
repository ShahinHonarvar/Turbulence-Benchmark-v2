def palindrome_of_length_n(text):
    list_of_letters = set()
    result = set()
    for letter in text:
        if letter.isalpha():
            list_of_letters.add(letter.lower())
    for i in range(len(list_of_letters) - 175):
        for j in range(i + 175, len(list_of_letters)):
            word = ''.join(list(list_of_letters)[i:j + 1])
            if word == word[::-1]:
                result.add(word)
    return result