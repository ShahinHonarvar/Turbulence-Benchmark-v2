def all_substring_of_size_n(arg):
    result = []
    for i in range(len(arg) - 2):
        substring = arg[i:i + 3]
        if substring == ''.join(sorted(substring)):
            if substring not in result:
                result.append(substring)
    return result