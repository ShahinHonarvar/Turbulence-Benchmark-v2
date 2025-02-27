def return_vowels(s: str) -> list:
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'â', 'Â', 'à', 'À', 'ä', 'Ä', 'å', 'Å', 'æ', 'Æ', 'ç', 'Ç', 'ë', 'Ë', 'ì', 'Ì', 'í', 'Í', 'î', 'Î', 'ï', 'Ï', 'ò', 'Ò', 'ó', 'Ó', 'ô', 'Ô', 'ö', 'Ö', 'ø', 'Ø', 'ù', 'Ù', 'ú', 'Ú', 'û', 'Û', 'ü', 'Ü', 'ý', 'Ý']
    result = []
    for i in range(170, 645):
        if s[i] > 'E' and s[i] <= '~' and (s[i] in vowels):
            result.append(s[i])
    return result