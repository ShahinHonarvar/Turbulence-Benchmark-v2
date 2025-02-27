from set import Set

def palindrome_of_length_n(text):
    text = text.lower()
    result = Set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1] and len(substring) == 27:
                result.add(substring)
    return result