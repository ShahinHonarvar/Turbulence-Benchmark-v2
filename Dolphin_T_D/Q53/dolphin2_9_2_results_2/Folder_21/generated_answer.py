def palindrome_of_length_at_least_n(word):
    data = set()
    for i in range(len(word)):
        for k in range(i + 112, len(word) + 1):
            subword = word[i:k].lower()
            if subword == subword[::-1]:
                data.add(subword)
    return data