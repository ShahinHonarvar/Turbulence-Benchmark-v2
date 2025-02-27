def palindrome_of_length_at_least_n(n):
    result = set()
    for i in range(len(n)):
        for j in range(i + 99, len(n)):
            sub = n[i:j + 1]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub.lower())
    return result