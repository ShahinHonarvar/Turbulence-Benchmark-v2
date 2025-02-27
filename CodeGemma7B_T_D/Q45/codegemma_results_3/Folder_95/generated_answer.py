def palindromes_between_indices(string):
    if len(string) < 8 or string[7] == string[8]:
        return set()
    if string[7] in ascii_lowercase and string[8] in ascii_lowercase:
        result = set()
        for i in range(ord(string[7]), ord(string[8]) + 1):
            for j in range(i, ord(string[8]) + 1):
                result.add(chr(i) + chr(j) + chr(i))
        return result
    return {string[7] + string[8] + string[7]}