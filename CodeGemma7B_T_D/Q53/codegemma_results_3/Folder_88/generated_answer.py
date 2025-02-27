def palindrome_of_length_at_least_n(s):
    word = s.lower()
    if len(word) < 27:
        return set()
    result = set()
    for i in range(len(word)):
        for j in range(i + 26, len(word) + 1):
            if word[i:j] == word[j - 2:i:-1]:
                result.add(word[i:j])
    return result