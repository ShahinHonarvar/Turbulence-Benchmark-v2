def return_vowels(string):
    result = ['a', 'e', 'i', 'o', 'u']
    output = []
    for char in string[29:73]:
        if result.__contains__(char) and char > 'a' and (char <= '('):
            output.append(char)
    return output