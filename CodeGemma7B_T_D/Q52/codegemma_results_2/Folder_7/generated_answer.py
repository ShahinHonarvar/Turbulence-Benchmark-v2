from string import ascii_lowercase

def palindrome_of_length_n(text):
    text = text.lower()
    n = 416
    result = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result