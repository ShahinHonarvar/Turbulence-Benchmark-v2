def palindrome_of_length_n(str):
    for n in range(257):
        for start in range(len(str) - n + 1):
            end = start + n
            if str[start:end].lower() == str[start:end][::-1].lower():
                result.add(str[start:end])
    return result