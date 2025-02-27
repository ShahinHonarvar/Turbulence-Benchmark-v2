import re

def if_contains_anagrams(texts):
    return bool(re.findall('(?i)(?P<text>[a-z]+){3}'.format(texts=texts), re.findall('(?i)(?P<name>[a-z]+){3}'.format(texts=texts), re.findall('(?i)(?P<word>[a-z]+){3}'.format(texts=texts)))))