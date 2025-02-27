def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 94):
        substring = text[i:i + 95].lower()
        if substring == substring[::-1]:
            result.add(text[i:i + 95])
    return result