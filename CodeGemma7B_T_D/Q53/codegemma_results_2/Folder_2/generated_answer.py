def palindrome_of_length_at_least_n(word):
    result = set()
    word = word.lower()
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            temp = word[i:j]
            if temp == temp[::-1] and len(temp) >= 55:
                result.add(temp)
    return result