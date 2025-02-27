def return_vowels(s, N, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for char in s[23:38]:
        if char > N and char <= k and (char in vowels):
            return_list.append(char)
    return return_list