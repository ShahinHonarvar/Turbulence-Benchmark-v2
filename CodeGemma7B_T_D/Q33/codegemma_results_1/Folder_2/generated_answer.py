def return_vowels(str):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for index, char in enumerate(str):
        if index >= 170 and index < 645 and (char in vowels) and (char > 'E') and (char <= '~'):
            result.append(char)
    return result