def palindromes_of_specific_lengths(s):
    s = s[20:75]
    ret_set = set()
    for length in range(36, 43):
        for i in range(len(s) - length + 1):
            temp = s[i:i + length]
            if temp.lower() == temp[::-1].lower():
                ret_set.add(temp)
    return ret_set