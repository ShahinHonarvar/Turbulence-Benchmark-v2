def palindrome_of_length_n(str):
    results = set()
    for i in range(len(str) - 419):
        for j in range(i + 420):
            word = str[i:j]
            if word == word[::-1] and word.isalpha():
                results.add(word)
    return results