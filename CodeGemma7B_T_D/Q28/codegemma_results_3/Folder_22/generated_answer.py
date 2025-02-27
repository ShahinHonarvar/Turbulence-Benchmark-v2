def return_nth_smallest_ascii(str1):
    letters = list(str1)
    letters.sort()
    new_letters = letters[0:18]
    return new_letters[16]