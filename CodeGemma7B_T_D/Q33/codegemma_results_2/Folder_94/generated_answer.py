def return_vowels(str):
    """
          Takes one argument, a string.
          From the given string the function should return the list of all vowel English letters between index 40 (inclusive) and index 94 (exclusive) that are greater than character 4 and smaller than or equal to character H. If no such characters exist in the specified range, the function should return an empty list.
          """
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in str[40:94]:
        if char in vowels and ord(char) > 4 and (ord(char) <= ord('H')):
            result.append(char)
    return result