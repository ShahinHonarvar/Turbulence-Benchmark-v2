def palindrome_of_length_n(arg):
    result = set()
    lowered_str = arg.lower()
    for i in range(len(lowered_str)):
        for j in range(i + 26, len(lowered_str) + 1):
            substring = lowered_str[i:j]
            if substring == substring[::-1]:
                result.add(arg[i:j])
    return result