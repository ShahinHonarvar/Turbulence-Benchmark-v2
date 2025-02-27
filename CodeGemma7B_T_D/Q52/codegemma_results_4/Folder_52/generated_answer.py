def palindrome_of_length_n(sub):
    result = set()
    for i in range(len(sub)):
        for j in range(i + 1, len(sub) + 1):
            temp_str = sub[i:j]
            if temp_str == temp_str[::-1] and len(temp_str) == 423 and temp_str.isalpha():
                result.add(temp_str)
    return result