def palindrome_of_length_n(arg):
    result = set()
    gibberish = [' ', '.', ',', '!', '?']
    for i in range(len(arg)):
        if arg[i] not in gibberish:
            for j in range(i + 1, len(arg)):
                if arg[j] not in gibberish:
                    temp = arg[i:j + 1]
                    temp = temp.lower()
                    temp = ''.join(sorted(temp))
                    if temp == temp[::-1] and len(temp) == 45:
                        result.add(temp)
    return result