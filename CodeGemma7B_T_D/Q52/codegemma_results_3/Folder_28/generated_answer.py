def palindrome_of_length_n(word):
    res = set()
    for i in range(len(word) - 42):
        temp = word[i:i + 43]
        temp = temp.lower()
        temp = temp[::-1]
        if temp == temp:
            res.add(word[i:i + 43])
    if len(res) > 0:
        return res
    else:
        return set()