def palindrome_of_length_n(string, n=392):
    result = set()
    for i in range(len(string) - n + 1):
        candidate = string[i:i + n].lower()
        if candidate == candidate[::-1]:
            result.add(candidate)
    return result if result else {''}