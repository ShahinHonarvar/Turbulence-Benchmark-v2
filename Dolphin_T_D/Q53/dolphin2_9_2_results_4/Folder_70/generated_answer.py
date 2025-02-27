def palindrome_of_length_at_least_n(word):
    n = 11
    result = set()
    for i in range(len(word)):
        for j in range(i + n, len(word) + 1):
            sub = word[i:j]
            if sub == sub.lower() == sub.upper() and sub == sub[::-1]:
                result.add(sub)
    return result