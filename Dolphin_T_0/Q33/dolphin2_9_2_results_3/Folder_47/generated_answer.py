def return_vowels(string, N, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(23, 38):
        if string[i] > N and string[i] <= k and (string[i] in vowels):
            result.append(string[i])
    return result