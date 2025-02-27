def palindrome_of_length_n(word, n):
    pallist = set()
    word = word.lower()
    for i in range(len(word) - n + 1):
        substr = word[i:i + n]
        if substr == substr[::-1]:
            pallist.add(substr)
    return pallist