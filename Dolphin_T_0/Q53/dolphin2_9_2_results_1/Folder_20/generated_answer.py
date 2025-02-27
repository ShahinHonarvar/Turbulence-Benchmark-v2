def palindrome_of_length_at_least_n(a_string):
    a_string = a_string.lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    result = set()
    for i in range(len(a_string) - 65):
        substring = a_string[i:i + 66]
        if set(substring).issubset(english_letters) and substring == substring[::-1]:
            result.add(substring)
    return result