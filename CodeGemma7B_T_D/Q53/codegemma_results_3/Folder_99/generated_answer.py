def palindrome_of_length_at_least_n(text):
    full = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            temp = text[i:j].lower()
            if temp == temp[::-1] and len(temp) >= 115 and temp.isalpha():
                full.add(temp)
    return full