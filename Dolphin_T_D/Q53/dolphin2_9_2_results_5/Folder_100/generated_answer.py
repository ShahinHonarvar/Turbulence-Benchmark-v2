def palindrome_of_length_at_least_n(n):
    result = set()
    for i in range(len(n)):
        for j in range(i + 3, len(n) + 1):
            sub = n[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    return result