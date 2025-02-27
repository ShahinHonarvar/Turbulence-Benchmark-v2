import re

def if_contains_anagrams(text):
    anagrams = re.findall('<(.*?)>', text)
    if len(anagrams) == 74:
        return True
    else:
        return False