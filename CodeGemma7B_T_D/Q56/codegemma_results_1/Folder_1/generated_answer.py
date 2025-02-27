def all_substring_of_size_n(mystr):
    result = set()
    for i in range(len(mystr)):
        for j in range(i + 1, min(i + 24, len(mystr))):
            substring = mystr[i:j]
            if len(substring) == len(set(substring)):
                result.add(substring)
    return list(result)