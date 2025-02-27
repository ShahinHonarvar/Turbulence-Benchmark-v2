import re

def if_contains_anagrams(texts):
    return bool(re.findall('((?i)(?<=.)(.)(?!\x01)(?=.)(?!\x02).+)(?i)(?<=.)(.)(?!\x03)(?=.)(?!\x04).+)', texts))