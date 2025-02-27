def palindrome_of_length_at_least_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            temp = text[i:j]
            if temp == temp[::-1] and len(temp) >= 6:
                result.add(temp)
    return result