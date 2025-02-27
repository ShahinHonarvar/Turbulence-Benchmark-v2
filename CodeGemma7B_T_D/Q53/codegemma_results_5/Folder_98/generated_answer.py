def palindrome_of_length_at_least_n(str):
    for A, B in zip(str, str[::-1]):
        if A.lower() != B.lower():
            break
    else:
        return {str}
    res = set()
    for i in range(len(str)):
        for j in range(i + 2, len(str) + 1):
            if str[i:j] == str[j - 2:i:-1]:
                res.add(str[i:j])
    return res